const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const context = vm.createContext({});
vm.runInContext(fs.readFileSync(__dirname + '/screening.js', 'utf8') + '\nthis.logic = LibraryLogic;', context);
const {filterRuns, sortRuns, coverage, ratingPlace, lowestRating, scale} = context.logic;
const keys = __dirname + '/../../../tests/fixtures/library-credit/';
const load = name => JSON.parse(fs.readFileSync(keys + name, 'utf8'));
const real = load('screening-catalogue.json').real;
const plain = value => JSON.parse(JSON.stringify(value));
const ids = rows => Array.from(rows, row => row.id);
const scaleKey = load('rating-scale.json');

test('code scale has the answer key rows in order', () => {
  assert.deepEqual(plain(scale), scaleKey.scale.map(row => row.moodys ? `${row.sp_fitch}/${row.moodys}` : row.sp_fitch));
});
for (const item of scaleKey.placement_cases) {
  test(`placement of ${JSON.stringify(item.text)}`, () => {
    const place = ratingPlace(item.text);
    if (item.off_scale) return assert.equal(place, null);
    assert.equal(place.rank, item.rank);
    assert.equal(place.placesAs, item.places_as);
  });
}
for (const item of scaleKey.lowest_cases) {
  test(`lowest rating: ${item.name}`, () => {
    const run = {ratings: item.ratings};
    const lowest = lowestRating(run, item.scope);
    assert.equal(lowest ? lowest.label : null, item.lowest);
    const below = (threshold) => filterRuns([{id: 'x', issuer: 'X', date: '2024-01-01', artifacts: [], metrics: {}, ratings: item.ratings}],
      {runs: 'any', ratingScope: item.scope, ratingBelow: threshold}).length === 1;
    for (const m of item.matches) assert.ok(below(m.threshold), m.threshold);
    for (const m of item.does_not_match) assert.ok(!below(m.threshold), m.threshold);
  });
}
for (const item of load('filter-cases.json')) {
  test(`filter case: ${item.name}`, () => {
    assert.deepEqual(ids(filterRuns(real, item.filters)).sort(), item.expected_ids);
    assert.deepEqual(plain(coverage(real, item.filters)), item.coverage || {});
  });
}
for (const item of load('sort-cases.json')) {
  test(`sort case: ${item.name}`, () => {
    assert.deepEqual(ids(sortRuns(filterRuns(real, item.filters), item.key, item.direction)), item.expected_ids);
  });
}

const issuerCase = load('issuer-case-cases.json');
for (const item of issuerCase.cases) {
  test(`issuer case folding: ${item.name}`, () => {
    const got = context.logic.screened(issuerCase.runs, item.filters);
    assert.deepEqual(ids(got.map(e => e.run)).sort(), [...item.expected_ids].sort());
    assert.deepEqual(got.filter(e => e.notScreened).map(e => e.run.id).sort(), [...item.expected_not_screened].sort());
  });
}

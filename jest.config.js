const { defaults: tsjPreset } = require('ts-jest/presets')

module.exports = {
  transform: tsjPreset.transform,
  clearMocks: true,
  collectCoverage: false,
  coverageDirectory: 'coverage',
  coverageProvider: 'v8',
  preset: '@shelf/jest-mongodb'
}

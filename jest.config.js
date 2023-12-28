const { defaults: tsjPreset } = require('ts-jest/presets')

module.exports = {
  transform: tsjPreset.transform,
  clearMocks: true,
  collectCoverage: false,
  coverageDirectory: 'coverage',
  preset: '@shelf/jest-mongodb',
  coverageProvider: 'v8',
  watchPathIgnorePatterns: ['globalConfig']
}

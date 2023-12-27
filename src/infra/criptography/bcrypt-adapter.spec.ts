import bcrypt from 'bcrypt'
import { BcryptAdapter } from './bcrypt-adapter'

jest.mock('bcrypt', () => ({
  async hash (): Promise<string> {
    return await new Promise(resolve => { resolve('hashed-value') })
  }
}))

describe('Bcrypt Adapter ', () => {
  test('Call bcrypt with correct values', async () => {
    // Arrange
    const salt = 12
    const sut = new BcryptAdapter(salt)

    // Arrange(Mock)
    const hashSpy = jest.spyOn(bcrypt, 'hash')

    // Act
    await sut.encrypt('any_value')

    // Assert
    expect(hashSpy).toHaveBeenCalledWith('any_value', salt)
  })
  test('Return a hash on success', async () => {
    // Arrange
    const salt = 12
    const sut = new BcryptAdapter(salt)

    // Act
    const hash = await sut.encrypt('any_value')

    // Assert
    expect(hash).toBe('hashed-value')
  })
})

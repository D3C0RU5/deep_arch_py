import bcrypt from 'bcrypt'
import { BcryptAdapter } from './bcrypt-adapter'

jest.mock('bcrypt', () => ({
  async hash (): Promise<string> {
    return await new Promise(resolve => { resolve('hashed-value') })
  }
}))

interface SutTypes {
  sut: BcryptAdapter
  salt: number
}

const makeSut = (): SutTypes => {
  const salt = 12
  const sut = new BcryptAdapter(salt)

  return { sut, salt }
}

describe('Bcrypt Adapter ', () => {
  test('Call bcrypt with correct values', async () => {
    // Arrange
    const { sut, salt } = makeSut()

    // Arrange(Mock)
    const hashSpy = jest.spyOn(bcrypt, 'hash')

    // Act
    await sut.encrypt('any_value')

    // Assert
    expect(hashSpy).toHaveBeenCalledWith('any_value', salt)
  })

  test('Return a hash on success', async () => {
    // Arrange
    const { sut } = makeSut()

    // Act
    const hash = await sut.encrypt('any_value')

    // Assert
    expect(hash).toBe('hashed-value')
  })

  test('Throw if bcrypt throws', async () => {
    // Arrange
    const { sut } = makeSut()

    // Arrange (mock)
    jest.spyOn<any, string>(bcrypt, 'hash').mockReturnValueOnce(new Promise((resolve, reject) => { reject(new Error()) }))

    // Act
    const promise = sut.encrypt('any_value')

    // Assert
    await expect(promise).rejects.toThrow()
  })
})

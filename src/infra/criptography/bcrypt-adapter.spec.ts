import bcrypt from 'bcrypt'
import { BcryptAdapter } from './bcrypt-adapter'

describe('Bcrypt Adapter ', () => {
  test('Should call bcrypt with correct values', async () => {
    // Arrange
    const salt = 12
    const sut = new BcryptAdapter(salt)

    // Arrange(Mock)
    const hashSpy = jest.spyOn(bcrypt, 'hash')

    // ACt
    await sut.encrypt('any_value')

    // Assert
    expect(hashSpy).toHaveBeenCalledWith('any_value', salt)
  })
})

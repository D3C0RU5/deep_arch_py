import { AccountMongoRepository } from './account'
import { MongoHelper } from './helpers/mongo-helper'

describe('Account Mongo Repository ', () => {
  beforeAll(async () => {
    await MongoHelper.connect(global.__MONGO_URI__)
  })

  afterAll(async () => {
    await MongoHelper.disconnect()
  })

  beforeEach(async () => {
    const accountCollection = MongoHelper.getCollection('accounts')
    await accountCollection.deleteMany({})
  })

  const makeSut = (): AccountMongoRepository => {
    return new AccountMongoRepository()
  }

  test('Return account on success', async () => {
    // Arrange
    const sut = makeSut()
    const account = await sut.add({
      name: 'any_name',
      email: 'any_email@mail.com',
      password: 'any_password'
    })

    // Assert
    expect(account).toBeTruthy()
    expect(account.id).toBeTruthy()
    expect(account.name).toBe('any_name')
    expect(account.email).toEqual('any_email@mail.com')
    expect(account.password).toEqual('any_password')
  })
})

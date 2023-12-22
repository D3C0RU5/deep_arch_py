import { InvalidParamError, MissingParamError, ServerError } from '../errors'
import { SignUpController } from './signup'
import { type EmailValidator } from '../protocols'
import { type AddAccountModel, type AddAccount } from '../../domain/usecases/add-account'
import { type AccountModel } from '../../domain/models/account'

const makeEmailValidator = (): EmailValidator => {
  class EmailValidatorStub implements EmailValidator {
    isValid (email: string): boolean {
      return true
    }
  }
  return new EmailValidatorStub()
}

const makeAccountStub = (): AddAccount => {
  class AddAccountStub implements AddAccount {
    add (account: AddAccountModel): AccountModel {
      const fakeAccount = {
        id: 'valid_id',
        name: 'valid_name',
        email: 'valid_email@mail.com',
        password: 'valid_password'
      }
      return fakeAccount
    }
  }

  return new AddAccountStub()
}

interface SutTypes {
  sut: SignUpController
  emailValidatorStub: EmailValidator
  addAccountStub: AddAccount
}

const makeSut = (): SutTypes => {
  const emailValidatorStub = makeEmailValidator()
  const addAccountStub = makeAccountStub()
  const sut = new SignUpController(emailValidatorStub, addAccountStub)

  return { sut, emailValidatorStub, addAccountStub }
}

describe('SignUp Controller', () => {
  test('Return 400 if no name is provided', () => {
    // Arrange
    const { sut } = makeSut()
    const httpRequest = {
      body: {
        email: 'any_email@mail.com',
        password: 'any_password',
        passwordConfirmation: 'any_password'
      }
    }

    // Act
    const httpResponse = sut.handle(httpRequest)

    // Assert
    expect(httpResponse.statusCode).toBe(400)
    expect(httpResponse.body).toEqual(new MissingParamError('name'))
  })

  test('Return 400 if no email is provided', () => {
    // Arrange
    const { sut } = makeSut()
    const httpRequest = {
      body: {
        name: 'any_name',
        password: 'any_password',
        passwordConfirmation: 'any_password'
      }
    }

    // Act
    const httpResponse = sut.handle(httpRequest)

    // Assert
    expect(httpResponse.statusCode).toBe(400)
    expect(httpResponse.body).toEqual(new MissingParamError('email'))
  })

  test('Return 400 if no password is provided', () => {
    // Arrange
    const { sut } = makeSut()
    const httpRequest = {
      body: {
        name: 'any_name',
        email: 'any_email@mail.com',
        passwordConfirmation: 'any_password'
      }
    }

    // Act
    const httpResponse = sut.handle(httpRequest)

    // Assert
    expect(httpResponse.statusCode).toBe(400)
    expect(httpResponse.body).toEqual(new MissingParamError('password'))
  })

  test('Return 400 if no password confirmation is provided', () => {
    // Arrange
    const { sut } = makeSut()
    const httpRequest = {
      body: {
        name: 'any_name',
        email: 'any_email@mail.com',
        password: 'any_password'
      }
    }

    // Act
    const httpResponse = sut.handle(httpRequest)

    // Assert
    expect(httpResponse.statusCode).toBe(400)
    expect(httpResponse.body).toEqual(new MissingParamError('passwordConfirmation'))
  })

  test('Return 400 if no password confirmation fails', () => {
    // Arrange
    const { sut } = makeSut()
    const httpRequest = {
      body: {
        name: 'any_name',
        email: 'any_email@mail.com',
        password: 'any_password',
        passwordConfirmation: 'invalid_password'
      }
    }

    // Act
    const httpResponse = sut.handle(httpRequest)

    // Assert
    expect(httpResponse.statusCode).toBe(400)
    expect(httpResponse.body).toEqual(new InvalidParamError('passwordConfirmation'))
  })

  test('Return 400 if an invalid email is provided', () => {
    // Arrange
    const { sut, emailValidatorStub } = makeSut()
    const httpRequest = {
      body: {
        name: 'any_name',
        email: 'invalid_email@mail.com',
        password: 'any_password',
        passwordConfirmation: 'any_password'
      }
    }

    // Arrange(Mock)
    jest.spyOn(emailValidatorStub, 'isValid').mockReturnValueOnce(false)

    // Act
    const httpResponse = sut.handle(httpRequest)

    // Assert
    expect(httpResponse.statusCode).toBe(400)
    expect(httpResponse.body).toEqual(new InvalidParamError('email'))
  })

  test('Call EmailValidator with correct email', () => {
    // Arrange
    const { sut, emailValidatorStub } = makeSut()
    const httpRequest = {
      body: {
        name: 'any_name',
        email: 'any_email@mail.com',
        password: 'any_password',
        passwordConfirmation: 'any_password'
      }
    }

    // Arrange(Mock)
    const isValidSpy = jest.spyOn(emailValidatorStub, 'isValid')

    // Act
    sut.handle(httpRequest)

    // Assert
    expect(isValidSpy).toHaveBeenCalledWith('any_email@mail.com')
  })

  test('Return 500 if EmailValidator throws', () => {
    // Arrange
    const { sut, emailValidatorStub } = makeSut()
    const httpRequest = {
      body: {
        name: 'any_name',
        email: 'any_email@mail.com',
        password: 'any_password',
        passwordConfirmation: 'any_password'
      }
    }

    // Arrange(Mock)
    jest.spyOn(emailValidatorStub, 'isValid').mockImplementationOnce(() => {
      throw new Error()
    })

    // Act
    const httpResponse = sut.handle(httpRequest)

    // Assert
    expect(httpResponse.statusCode).toBe(500)
    expect(httpResponse.body).toEqual(new ServerError())
  })

  test('Call AddAccount with correct values', () => {
    // Arrange
    const { sut, addAccountStub } = makeSut()
    const httpRequest = {
      body: {
        name: 'any_name',
        email: 'any_email@mail.com',
        password: 'any_password',
        passwordConfirmation: 'any_password'
      }
    }

    // Arrange(Mock)
    const addSpy = jest.spyOn(addAccountStub, 'add')

    // Act
    sut.handle(httpRequest)

    // Assert
    expect(addSpy).toHaveBeenCalledWith({
      name: 'any_name',
      email: 'any_email@mail.com',
      password: 'any_password'
    })
  })
})

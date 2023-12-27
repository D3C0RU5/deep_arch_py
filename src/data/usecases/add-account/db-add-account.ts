import {
  type AddAccountRepository,
  type AccountModel,
  type AddAccount,
  type AddAccountModel,
  type Encrypter
} from './db-add-account.protocols'

export class DbAddAccount implements AddAccount {
  private readonly encrypter: Encrypter
  private readonly addAccountRepository: AddAccountRepository

  constructor (encrypter: Encrypter, addAccountRepository: AddAccountRepository) {
    this.encrypter = encrypter
    this.addAccountRepository = addAccountRepository
  }

  add = async (accountData: AddAccountModel): Promise<AccountModel> => {
    const hashedPassword = await this.encrypter.encrypt(accountData.password)
    const newAccount: AccountModel = await this.addAccountRepository.add(
      Object.assign(
        {},
        accountData,
        { password: hashedPassword }
      ))
    return await new Promise(resolve => { resolve(newAccount) })
  }
}

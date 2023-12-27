import { type AccountModel, type AddAccount, type AddAccountModel, type Encrypter } from './db-add-account.protocols'

export class DbAddAccount implements AddAccount {
  private readonly encrypter: Encrypter
  constructor (encrypter: Encrypter) {
    this.encrypter = encrypter
  }

  add = async (account: AddAccountModel): Promise<AccountModel> => {
    const hashedPassword = await this.encrypter.encrypt(account.password)
    const newAccount: AccountModel = { id: '1', name: 'name', email: 'email', password: hashedPassword }
    return await new Promise(resolve => { resolve(newAccount) })
  }
}

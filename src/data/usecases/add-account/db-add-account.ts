import { type AccountModel } from '../../../domain/models/account'
import { type AddAccountModel, type AddAccount } from '../../../domain/usecases/add-account'
import { type Encrypter } from '../../protocols/encrypter'

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

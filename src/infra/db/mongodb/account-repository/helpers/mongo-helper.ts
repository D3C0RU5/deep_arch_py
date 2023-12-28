import { type Collection, MongoClient, Db } from 'mongodb'

export const MongoHelper = {
  client: MongoClient,
  db: Db,
  async connect (url: string): Promise<void> {
    this.client = await MongoClient.connect(globalThis.__MONGO_URI__)
    this.db = await this.client.db(globalThis.__MONGO_DB_NAME__)
  },
  async disconnect (): Promise<void> {
    await this.client.close()
  },
  getCollection (name: string): Collection {
    return this.db.collection(name)
  }
}

import * as dotenv from "dotenv"
import { fastify } from "fastify"

import fastifyRedis from "@fastify/redis"

dotenv.config()

const server = fastify()
const { redis } = fastify()

server.register(fastifyRedis, {
  client: redis,
  closeClient: true,
})

const start = async () => {
  try {
    await server.listen({
      port: (process.env.PORT as unknown as number) || 4000,
    })
    console.log("Server started successfully!")
  } catch (err) {
    server.log.error(err)
    process.exit(1)
  }
}

start()

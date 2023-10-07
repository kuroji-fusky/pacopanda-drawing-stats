import { NextResponse } from "next/server"
import type { NextRequest } from "next/server"

export default function middleware(request: NextRequest) {
  const requestHeaders = new Headers(request.headers)
  const generatedNonce = crypto.randomUUID()

  requestHeaders.set("x-nonce", generatedNonce)

  const response = NextResponse.next({
    request: {
      headers: requestHeaders,
    },
  })

  response.headers.set("Content-Encoding", "br")
  response.headers.set("X-Content-Type-Options", "no-sniff")

  return response
}

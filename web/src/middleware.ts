import { NextResponse } from "next/server"
import type { NextRequest } from "next/server"

export default function middleware(request: NextRequest) {
  const requestHeaders = new Headers(request.headers)
  const generatedNonce = crypto.randomUUID()

  // Set the CSP header so that Next.js can read it and generate tags with the nonce
  // TODO import generateCSP() to the utils submodule
  // requestHeaders.set("Content-Security-Policy", csp)
  requestHeaders.set("x-nonce", generatedNonce)

  const response = NextResponse.next({
    request: {
      headers: requestHeaders
    }
  })

  response.headers.set("Content-Encoding", "br")
  // response.headers.set("Content-Security-Policy", csp)
  response.headers.set("X-Content-Type-Options", "no-sniff")
  response.headers.set("X-Frame-Options", "DENY")
  /**
   ** Technically not supported by most browsers as it's a non-standard, but it's here
   ** just for good measure.
   **/
  response.headers.set("X-XSS-Protection", "1; mode=block")

  return response
}

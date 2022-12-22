import { useEffect } from "react"

export default function useAppendHTML(...className: string[]) {
  useEffect(() => {
    if (typeof window !== "undefined") {
      const htmlRoot = document.documentElement
      htmlRoot.classList.add(...className)
    }
  }, [])
}

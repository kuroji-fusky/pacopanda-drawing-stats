module.exports = {
  extends: ["next", "prettier", "next/core-web-vitals"],
  plugins: ["prettier"],
  settings: {
    next: {
      rootDir: ["apps/*/", "packages/*/"],
    },
  },
  rules: {
    "@next/next/no-html-link-for-pages": "off",
    "no-unused-vars": "error",
    "no-irregular-whitespace": "error",
    "no-trailing-spaces": "error",
    "no-empty-function": "error",
    "no-duplicate-imports": "error",
  },
};
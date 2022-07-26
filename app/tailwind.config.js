const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1366px",
      "2xl": "1536px"
    },
    fontFamily: {
      heading: ["Noto Sans", ...defaultTheme.fontFamily.sans],
      body: ["Lato", ...defaultTheme.fontFamily.sans],
      mono: ["Fira Code", "Ubuntu Mono", ...defaultTheme.fontFamily.mono],
    },
    zIndex: {
      1: '1',
      2: '2',
      3: '3',
      'mosttop': '9999',
    },
    borderRadius: {
      'sm': '.125rem',
      'md': '6px',
      'full': '50%',
    },
    extend: {},
    plugins: [],
  }
}
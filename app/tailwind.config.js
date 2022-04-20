module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  purge: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  theme: {
    screens: {
      sm: '640px',
      md: '768px',
      max_md: { max: '767px' },
      lg: '1024px',
      xl: '1536px'
    },
    fontFamily: {
      title: ['Dancing Script', 'sans-serif'],
    },
    zIndex: {
      1: -1,
    },
    extend: {},
  },
  plugins: [],
}

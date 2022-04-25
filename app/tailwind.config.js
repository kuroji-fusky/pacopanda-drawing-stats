module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    screens: {
      sm: '640px',
      md: '768px',
      max_md: { max: '767px' },
      lg: '1024px',
      xl: '1536px'
    },
    theme: {
      fontFamily: {
        display: ["Noto Sans KR", 'system-ui', 'sans-serif'],
        body: ["Lato", 'system-ui', 'sans-serif'],
      },
      zIndex: {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'mosttop': '9999',
      },
      borderRadius: {
        'sm': '.125rem',
        'md': '6px',
        'full': '50%',
      },
    extend: {},
  },
  plugins: [],
}

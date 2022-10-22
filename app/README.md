# Nextwind (Next.js + Tailwind CSS) starter template

For me,
Setting up Sass and TailwindCSS can be a hassle already in contrast to just setting a plain
Next.js project. I'm tired of setting things up with my favorite CSS preprocessor and
framework can be almost time-consuming to get things up and running; so here's a template
I made to make this entire process a whole lot easier! :3

## Dependencies

- `nextjs`
- `sass`
- `tailwindcss`
- `autoprefixer`
- `postcss`

## Process

Init `next-app` with yarn

```console
yarn create next-app next-app --typescript
cd next-app
```

Install Sass and TailwindCSS

```console
yarn add -D sass tailwindcss autoprefixer postcss
```

Configured Tailwind stuff according to the [Tailwind Next.js docs](https://tailwindcss.com/docs/guides/nextjs)

```console
npx tailwindcss init -p
```

```diff
module.exports = {
+ content: [
+   "./pages/**/*.{js,ts,jsx,tsx}",
+   "./components/**/*.{js,ts,jsx,tsx}",
+ ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Then I renamed the `.css` files to `.scss` files and that's it!

All you have to do is start the dev server and you're ready to make the next big thing!

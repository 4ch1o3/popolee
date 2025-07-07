/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./components/**/*.{js,jsx,ts,tsx}"],

  theme: {
    extend: {
      colors: {
        primary: "#2F323C",
        secondary: "#FBFAF9",
        tertiery: "#7C8195",
        "text-placeholder": "#999999",
        "search-bg": "#EFEFEF",
        error: "#BE3030",
        like: "#D16D6D",
        "form-bg": "rgba(255, 255, 255, 0.8)",
        "img-placeholder-green": "#C3D8BF",
        "img-placeholder-pink": "#E0C9C9",
        "img-placeholder-blue": "#CDD7E2",
        "img-placeholder-purple": "#DED8E9",
        "img-placeholder-orange": "#D9CDBE",
        "img-placeholder-yellow": "#D9D4BE",
      },
      fontFamily: {
        pretendard: ["Pretendard", "sans-serif"],
      },
    },
  },

  plugins: [],
};

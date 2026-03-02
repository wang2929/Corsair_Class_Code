import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  base: "/Corsair_Class_code", //< DON'T ADD A CLOSING SLASH
  plugins: [react(), tailwindcss()],
})

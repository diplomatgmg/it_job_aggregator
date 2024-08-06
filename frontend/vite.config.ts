import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import path from "path"

export default defineConfig(() => {
  return {
    plugins: [react()],
    server: {
      port: 3000,
      host: "0.0.0.0",
    },
    resolve: {
      alias: [{ find: "@", replacement: path.resolve(__dirname, "src") }],
    },
  }
})

import { type ReactElement } from "react"
import Home from "@/features/home/components/Home.tsx"
import CommonPage from "@/components/layout/CommonPage.tsx"

const HomePage = (): ReactElement => {
  return (
    <CommonPage>
      <Home />
    </CommonPage>
  )
}

export default HomePage

import { type ReactElement } from "react"
import useAuth from "@/store/hooks/useAuth.ts"
import routes from "@/routes/routes.tsx"
import Button from "@/components/common/Button.tsx"
import Link from "@/components/common/Link.tsx"
import { colors } from "@/styles/theme.ts"
import useLogout from "@/store/hooks/useLogout.ts"
import styled, { ThemeProvider } from "styled-components"
import { useLocation } from "react-router-dom"

const HeaderNavigation = (): ReactElement => {
  const { isAuthenticated } = useAuth()
  const logoutHandler = useLogout()
  const location = useLocation()

  const renderLink = (to: string, label: string) => {
    return (
      <ThemeProvider theme={{ isActive: location.pathname === to }}>
        <HeaderItemStyle>
          <Link to={to}>{label}</Link>
        </HeaderItemStyle>
      </ThemeProvider>
    )
  }

  return (
    <HeaderListStyle>
      {renderLink(routes.home.path, "Home")}

      {isAuthenticated && renderLink(routes.profile.path, "Profile")}

      {renderLink(routes.faq.path, "FAQ")}

      {isAuthenticated && (
        <AuthButtonContainer>
          <Button
            onClick={logoutHandler}
            borderRadius="0"
            backgroundColor={colors.danger}>
            Logout
          </Button>
        </AuthButtonContainer>
      )}

      {!isAuthenticated && (
        <AuthButtonContainer>
          {renderLink(routes.login.path, "Login")}
          {renderLink(routes.register.path, "Register")}
        </AuthButtonContainer>
      )}
    </HeaderListStyle>
  )
}

interface HeaderItemProps {
  theme: {
    isActive: boolean
  }
}

const HeaderListStyle = styled.ul`
  display: flex;
  position: fixed;
  flex-direction: column;
  padding: 0;
  height: 100%;
  background-color: ${colors.background};
  margin: 0;
`

const HeaderItemStyle = styled.div<HeaderItemProps>`
  width: 200px;
  position: relative;
  background-color: ${({ theme }) =>
    theme.isActive ? colors.primary : colors.accent};

  a {
    padding: 1.25rem 0;
    background-color: ${({ theme }) =>
      theme.isActive ? colors.primary : colors.accent};

    &:hover {
      background-color: ${colors.primary};
    }
  }
`

const AuthButtonContainer = styled(HeaderItemStyle)`
  margin-top: auto;
  padding: 0;
`

export default HeaderNavigation

import { configureStore } from "@reduxjs/toolkit"
import authApi from "@/store/api/authApi.ts"
import hardSkillApi from "@/store/api/hardSkillApi.ts"
import authReducer from "@/store/slice/authSlice.ts"

const store = configureStore({
  reducer: {
    [authApi.reducerPath]: authApi.reducer,
    [hardSkillApi.reducerPath]: hardSkillApi.reducer,
    auth: authReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(authApi.middleware, hardSkillApi.middleware),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch

export default store

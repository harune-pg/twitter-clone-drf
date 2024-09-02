import axios from "axios";

const instance = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
});

const getUser = async () => {
  try {
    const response = await instance.get("/accounts/user");
    console.log(response);
  } catch (e) {
    console.error(e);
  }
}

export { getUser };

import axios from "axios";

const getUser = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/api/accounts/user/",
    );
    console.log(response);
  } catch (e) {
    console.error(e);
  }
}

export { getUser };

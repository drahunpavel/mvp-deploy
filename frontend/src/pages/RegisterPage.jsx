import axios from "axios";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const RegisterPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("/auth-api/register", {
        username,
        password,
      });
      alert("Регистрация успешна!");
      console.log(res.data);
      window.sessionStorage.setItem("access_token", res.data.access_token);
      navigate("/");
    } catch (err) {
      alert("Ошибка регистрации");
      console.error(err);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Регистрация</h1>
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-sm bg-white p-6 rounded shadow"
      >
        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Логин"
          required
          className="w-full p-2 mb-4 border rounded"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Пароль"
          required
          className="w-full p-2 mb-4 border rounded"
        />
        <button
          type="submit"
          className="w-full bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
        >
          Зарегистрироваться
        </button>
      </form>
      <p className="mt-4">
        Есть аккаунт?{" "}
        <a href="/login" className="text-blue-500">
          Войти
        </a>
      </p>
    </div>
  );
};

export default RegisterPage;

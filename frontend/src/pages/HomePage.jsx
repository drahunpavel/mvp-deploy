import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const [item, setItem] = useState(null);

  const navigate = useNavigate();

  useEffect(() => {
    const fetchInfo = async () => {
      try {
        const res = await axios.get("/ui-api/info", {
          headers: {
            Authorization: `Bearer ${window.sessionStorage.getItem(
              "access_token"
            )}`,
          },
        });
        console.log(res.data);
        setItem({ ...res.data });
      } catch (err) {
        console.error(err);
        navigate("/login");
      }
    };

    fetchInfo();
  }, [navigate]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-4xl font-bold mb-4">Добро пожаловать!</h1>
      <div className="container mx-auto text-left">
        {item?.client_ip && (
          <p className="mb-0">
            <b>ip:</b> {item.client_ip}
          </p>
        )}
        {item?.username && (
          <p className="mb-0">
            <b>user name:</b> {item.username}
          </p>
        )}
        {item?.user_agent && (
          <p className="mb-0">
            <b>user agent:</b> {item.user_agent}
          </p>
        )}
      </div>
    </div>
  );
};

export default HomePage;

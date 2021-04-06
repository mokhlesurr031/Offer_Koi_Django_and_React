import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import Hello from "./components/Head";
import FetchShopData from "./components/FetchShopData";
import PostShopData from "./components/PostShopData";

ReactDOM.render(
  <React.StrictMode>
    <Hello />
    <App />
    <PostShopData />
    <FetchShopData />
  </React.StrictMode>,
  document.getElementById("root")
);

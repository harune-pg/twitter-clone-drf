import React from "react";
import { createRoutesFromElements, createBrowserRouter, Route, RouterProvider } from "react-router-dom";
import Sample from "./routes/sample";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="sample/" element={<Sample />} />
  )
);

export default function App() {
  return (
    <RouterProvider router={router} />
  );
}

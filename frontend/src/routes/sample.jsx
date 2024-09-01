import React, { useEffect } from "react";
import { getUser } from "../api/sampleApi";

const Sample = () => {
  useEffect(() => {
    // ページがマウントされた時にgetUser関数を呼び出す
    const fetchData = async () => {
      await getUser();
    };
    // 現時点では401エラーが返ってくる
    fetchData();
  });

  return (
    <div>
      <p>Sample</p>
    </div>
  );
}

export default Sample;

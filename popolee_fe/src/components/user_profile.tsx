import React from "react";

export const UserProfile = () => {
  return (
    <a href={`./user=${"userId"}`}>
      <div className="w-8 h-8 rounded-full bg-img-placeholder-blue"></div>
    </a>
  );
};

export const FullProfile = () => {
  const image_count = 0;
  return (
    <div className="flex flex-col gap-10 mb-8">
      <div className="flex gap-4 items-center">
        <div className="w-17.5 h-17.5 bg-img-placeholder-blue rounded-full" />
        <>
          <p className="large-title">username</p>
        </>
      </div>
      <p className="subtitle">내가 올린 포즈 ({image_count})</p>
    </div>
  );
};

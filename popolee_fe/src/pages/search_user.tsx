import { TopBar } from "../components/top_bar";

export const SearchUser = () => {
  return (
    <div className="flex flex-col gap-3">
      <TopBar showSearch={true} showProfile={true} />
      <div className="flex justify-between items-center gap-4">
        <input
          placeholder="사용자 검색"
          className=" bg-search-bg text-primary border-0 focus:outline-1 outline-tertiery rounded-(--radius-sm) px-2 py-1.5 w-full detail"
        ></input>
        <a href="/" className="no-underline text-primary content shrink-0">
          <p>취소</p>
        </a>
      </div>
    </div>
  );
};

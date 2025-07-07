import { Routes, Route } from "react-router-dom";
import { TopBar } from "./components/top_bar";
import { SearchUser } from "./pages/search_user";
import { FilterList } from "./components/filter_list";
import { BottomBar } from "./components/bottom_bar";
import SadFace from "./assets/icons/SadFace.svg";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Feed />}></Route>
      <Route path="/search_user" element={<SearchUser />}></Route>
      <Route path="/mypage" />;<Route path="*" element={<ErrorPage />}></Route>
    </Routes>
  );
}

// main structure = topbar + bottombar
// only switch contents? (+ pass page info to topbar, hide/show search/profile)
const Feed = () => {
  return (
    <>
      {/* app bar */}
      <div>
        <TopBar showProfile={true} showSearch={true} />
        <FilterList />
      </div>

      {/* image list */}
      <div className="feed"></div>
      {/* bottom bar */}
      <BottomBar />
    </>
  );
};

const ErrorPage = () => {
  return (
    <div className="h-full">
      <TopBar showSearch={false} showProfile={false} />
      <div className="flex flex-col items-center h-9/10 justify-between p-16">
        <div className="w-9/10 h-1/3">
          <img src={SadFace} className="w-full h-full opacity-20"></img>
        </div>
        <div className="flex flex-col text-center gap-4">
          <p className="large-title text-primary">404</p>
          <p className="content text-primary">존재하지 않는 페이지입니다.</p>
        </div>
        <a href="/" className="no-underline">
          <p className="w-fit px-4 py-2 border-1 rounded-full inline-block align-baseline content border-tertiery text-tertiery bg-secondary hover:bg-search-bg ">
            피드로 돌아가기
          </p>
        </a>
      </div>
    </div>
  );
};

export default App;

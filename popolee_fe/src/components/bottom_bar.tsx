import UploadIcon from "../assets/UploadButton.svg";

export const BottomBar = () => {
  return (
    <div className="bg-secondary absolute bottom-0 left-0 w-full flex justify-center h-23">
      <div className=" bg-secondary w-fit p-1.5 rounded-full absolute bottom-13">
        <a href="./upload">
          <img src={UploadIcon} className="inline-block align-middle"></img>
        </a>
      </div>
    </div>
  );
};

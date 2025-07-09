type Image = {
  id: number;
  path: string;
  width: number;
  height: number;
};

type ImageList = {
  images: Image[];
};

export const ImageListUI = () => {
  const imageList: ImageList = {
    images: [
      {
        id: 1,
        width: 100,
        height: 300,
        path: "",
      },
      {
        id: 2,
        width: 300,
        height: 100,
        path: "",
      },
      {
        id: 3,
        width: 300,
        height: 200,
        path: "",
      },
      {
        id: 4,
        width: 200,
        height: 300,
        path: "",
      },
    ],
  };

  return (
    <div className="w-full py-4">
      {imageList.images.map((image: Image) => (
        <div
          key={image.id}
          className="bg-img-placeholder-blue"
          style={{ width: `${image.width}px`, height: `${image.height}px` }}
        ></div>
      ))}
    </div>
  );
};

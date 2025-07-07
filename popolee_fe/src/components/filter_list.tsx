import { Chip } from "./chip";

export const FilterList = () => {
  return (
    <div className="gap-2 flex w-fit mt-3">
      <Chip label="3명" type="Person" showIcon onClick={() => {}}></Chip>
      <Chip label="최신 순" type="Sort" showIcon onClick={() => {}}></Chip>
      <Chip label="태그" type="Tag" showIcon onClick={() => {}}></Chip>
    </div>
  );
};

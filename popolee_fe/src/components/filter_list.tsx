import { useState } from "react";
import { Chip } from "./chip";

export type chipType = "Person" | "Sort" | "Tag";

export const FilterList = () => {
  const [selectedChip, setSelectedChip] = useState<chipType | null>(null);

  const handleSelection = (type: chipType) => {
    setSelectedChip((prev) => (prev === type ? null : type));
  };

  return (
    <div className="gap-2 flex w-fit mt-3">
      <Chip
        label="3명"
        type="Person"
        showIcon
        onClick={() => handleSelection("Person")}
        isSelected={selectedChip === "Person"}
      />
      <Chip
        label="최신 순"
        type="Sort"
        showIcon
        onClick={() => handleSelection("Sort")}
        isSelected={selectedChip === "Sort"}
      />
      <Chip
        label="태그"
        type="Tag"
        showIcon
        onClick={() => handleSelection("Tag")}
        isSelected={selectedChip === "Tag"}
      />
    </div>
  );
};

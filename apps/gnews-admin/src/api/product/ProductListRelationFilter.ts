import { ProductWhereInput } from "./ProductWhereInput";

export type ProductListRelationFilter = {
  every?: ProductWhereInput;
  some?: ProductWhereInput;
  none?: ProductWhereInput;
};

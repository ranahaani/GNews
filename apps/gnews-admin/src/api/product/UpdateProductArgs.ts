import { ProductWhereUniqueInput } from "./ProductWhereUniqueInput";
import { ProductUpdateInput } from "./ProductUpdateInput";

export type UpdateProductArgs = {
  where: ProductWhereUniqueInput;
  data: ProductUpdateInput;
};

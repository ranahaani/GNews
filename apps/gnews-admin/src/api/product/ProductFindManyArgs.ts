import { ProductWhereInput } from "./ProductWhereInput";
import { ProductOrderByInput } from "./ProductOrderByInput";

export type ProductFindManyArgs = {
  where?: ProductWhereInput;
  orderBy?: Array<ProductOrderByInput>;
  skip?: number;
  take?: number;
};

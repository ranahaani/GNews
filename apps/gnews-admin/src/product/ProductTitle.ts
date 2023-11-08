import { Product as TProduct } from "../api/product/Product";

export const PRODUCT_TITLE_FIELD = "name";

export const ProductTitle = (record: TProduct): string => {
  return record.name?.toString() || String(record.id);
};

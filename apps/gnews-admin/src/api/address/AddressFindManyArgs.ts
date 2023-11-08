import { AddressWhereInput } from "./AddressWhereInput";
import { AddressOrderByInput } from "./AddressOrderByInput";

export type AddressFindManyArgs = {
  where?: AddressWhereInput;
  orderBy?: Array<AddressOrderByInput>;
  skip?: number;
  take?: number;
};

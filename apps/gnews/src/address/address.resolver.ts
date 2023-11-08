import * as graphql from "@nestjs/graphql";
import { AddressResolverBase } from "./base/address.resolver.base";
import { Address } from "./base/Address";
import { AddressService } from "./address.service";

@graphql.Resolver(() => Address)
export class AddressResolver extends AddressResolverBase {
  constructor(protected readonly service: AddressService) {
    super(service);
  }
}

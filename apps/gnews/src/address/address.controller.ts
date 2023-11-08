import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import { AddressService } from "./address.service";
import { AddressControllerBase } from "./base/address.controller.base";

@swagger.ApiTags("addresses")
@common.Controller("addresses")
export class AddressController extends AddressControllerBase {
  constructor(protected readonly service: AddressService) {
    super(service);
  }
}

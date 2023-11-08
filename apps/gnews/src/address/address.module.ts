import { Module } from "@nestjs/common";
import { AddressModuleBase } from "./base/address.module.base";
import { AddressService } from "./address.service";
import { AddressController } from "./address.controller";
import { AddressResolver } from "./address.resolver";

@Module({
  imports: [AddressModuleBase],
  controllers: [AddressController],
  providers: [AddressService, AddressResolver],
  exports: [AddressService],
})
export class AddressModule {}

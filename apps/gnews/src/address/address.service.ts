import { Injectable } from "@nestjs/common";
import { PrismaService } from "../prisma/prisma.service";
import { AddressServiceBase } from "./base/address.service.base";

@Injectable()
export class AddressService extends AddressServiceBase {
  constructor(protected readonly prisma: PrismaService) {
    super(prisma);
  }
}

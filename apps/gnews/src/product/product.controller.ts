import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import { ProductService } from "./product.service";
import { ProductControllerBase } from "./base/product.controller.base";

@swagger.ApiTags("products")
@common.Controller("products")
export class ProductController extends ProductControllerBase {
  constructor(protected readonly service: ProductService) {
    super(service);
  }
}

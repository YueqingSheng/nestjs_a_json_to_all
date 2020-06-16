# nestjs_a_json_to_all
Pass a json and get all crud apis and swagger documents.
Developed based on @nestjx/crud
## Prerequisite
python > 3.7

intsall ipython

install @nest/cli

install @nestjx/crud

install @nestjs/swagger

put beg.py into your nestjs project folder

## Run
ipython beg.py your_entity_name.json
## Json
your_entity.json contains the structure of your entity, it looks exactly same as the json you sent to server or responsed.

For example:

**test.json**

        {"name": "hi", "age": 1}

This json will convert to an entity file like this:

**test.entity.ts**
```typescript
export class Test {
        @PrimaryGeneratedColumn()
        @ApiModelProperty()
        id: number;

        @Column()
        @ApiModelProperty()
        name: string;

        @Column()
        @ApiModelProperty()
        age: number;
}
```
**Swagger**

![](https://yueqingsheng.github.io/post-images/1588622024790.png)
